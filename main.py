import streamlit as pd_stream
import os
import shutil
from app.database import SessionLocal
from app.processor import extract_text_from_pdf
from app.extractor import extract_structured_data
from app.crud import save_invoice_extraction
from app.logger import logger

# Set up page configurations for a clean enterprise feel
pd_stream.set_page_config(
    page_title="Structured JSON Invoice Extractor",
    page_icon="🧾",
    layout="wide"
)

pd_stream.title("🧾 Enterprise Invoice Data Extraction Engine")
pd_stream.markdown(
    "Upload raw PDF invoices to automatically parse structural text fields, run validation layers with Gemini 1.5 Flash, and archive transactions directly to your system database."
)

pd_stream.divider()

# Create a clear two-column operational layout
left_upload_panel, right_results_panel = pd_stream.columns([1, 1.2])

with left_upload_panel:
    pd_stream.header("📥 Document Upload Panel")
    uploaded_file = pd_stream.file_uploader(
        "Drop your corporate invoice PDF here...", 
        type=["pdf"], 
        help="Supports digital text-layer PDF documents."
    )
    
    if uploaded_file is not None:
        pd_stream.success(f"File uploaded successfully: {uploaded_file.name}")
        
        # Trigger Extraction Process Engine on Click
        if pd_stream.button("🚀 Execute Data Extraction Pipeline", use_container_width=True):
            
            # Create a temporary storage folder to write the uploaded bytes to disk
            temp_directory = "temp_processing"
            os.makedirs(temp_directory, exist_ok=True)
            temp_file_path = os.path.join(temp_directory, uploaded_file.name)
            
            with open(temp_file_path, "wb") as buffer:
                buffer.write(uploaded_file.getbuffer())
                
            # Initialize interactive, layered progress bars
            with pd_stream.status("Processing document pipeline...", expanded=True) as status_box:
                try:
                    status_box.update(label="Step 1/3: Ripping text layers from PDF binary...", state="running")
                    extracted_text = extract_text_from_pdf(temp_file_path)
                    
                    status_box.update(label="Step 2/3: Marshalling AI Orchestration Brain (Gemini)...", state="running")
                    validated_invoice_json = extract_structured_data(extracted_text)
                    
                    status_box.update(label="Step 3/3: Committing transactional record to database...", state="running")
                    db_connection = SessionLocal()
                    try:
                        saved_db_record = save_invoice_extraction(
                            db=db_connection, 
                            extraction_data=validated_invoice_json, 
                            raw_text=extracted_text
                        )
                    finally:
                        db_connection.close()
                        
                    status_box.update(label="Pipeline Completed Successfully!", state="complete")
                    
                    # Store variables inside the UI session memory to draw the right column
                    pd_stream.session_state["extraction_results"] = validated_invoice_json
                    pd_stream.session_state["db_id"] = saved_db_record.id
                    
                except Exception as system_fault:
                    status_box.update(label="Pipeline Terminated Due to System Fault", state="error")
                    pd_stream.error(f"Execution Stopped: {str(system_fault)}")
                    logger.critical(f"UI Interface Layer Crash: {str(system_fault)}")
                finally:
                    # Clean up the local temp folder immediately to keep directory sanitary
                    if os.path.exists(temp_directory):
                        shutil.rmtree(temp_directory)

with right_results_panel:
    pd_stream.header("📊 Validated JSON Schema Output")
    
    # Check if data has been processed in this session
    if "extraction_results" in pd_stream.session_state:
        results = pd_stream.session_state["extraction_results"]
        record_id = pd_stream.session_state["db_id"]
        
        pd_stream.metric(label="Database Archive Record ID", value=f"#{record_id}")
        
        # Display Key Information Summary Cards
        card_col1, card_col2, card_col3 = pd_stream.columns(3)
        card_col1.text_input("Vendor Name", value=results.vendor_name, disabled=True)
        card_col2.text_input("Invoice #", value=results.invoice_number, disabled=True)
        card_col3.text_input("Invoice Date", value=results.invoice_date, disabled=True)
        
        financial_col1, financial_col2 = pd_stream.columns(2)
        financial_col1.metric(label="Subtotal Amount", value=f"${results.subtotal:,.2f}")
        financial_col2.metric(label="Total Amount Due", value=f"${results.total_amount:,.2f}")
        
        # Render the full Pydantic JSON structure raw on the dashboard screen
        pd_stream.subheader("Raw Structural JSON Breakdown")
        pd_stream.json(results.model_dump())
        
    else:
        pd_stream.info("Awaiting file ingestion pipeline. Upload an invoice to view structured tracking arrays.")
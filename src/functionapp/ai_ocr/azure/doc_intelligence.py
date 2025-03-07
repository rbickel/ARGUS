import json
import pandas as pd
from azure.core.credentials import AzureKeyCredential
from azure.identity import DefaultAzureCredential
from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.ai.documentintelligence.models import DocumentAnalysisFeature
from ai_ocr.azure.config import get_config


config = get_config()

credential = DefaultAzureCredential()
if(config["doc_intelligence_key"] != ""):
    credential = AzureKeyCredential(config["doc_intelligence_key"])

document_intelligence_client = DocumentIntelligenceClient(endpoint=config["doc_intelligence_endpoint"],
                                                            credential=AzureKeyCredential(config["doc_intelligence_key"]),
                                                            headers={"solution":"ARGUS-1.0"})

def get_ocr_results(file_path: str):
    with open(file_path, "rb") as f:
        poller = document_intelligence_client.begin_analyze_document("prebuilt-layout", 
                                                                        body=f)

    ocr_result = poller.result().content
    return ocr_result


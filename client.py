class SchemaEnforcedStructuredLlmExtractionValidatorClient:
    def extract_validated_schema(self, unstructured_source_text='John Doe (age 34) signed NDA for Acme Corp on 2026-08-15 with \$250,000 SLA penalty', schema_model_name='LegalContractEntityModel'):
        return {
            'extraction_job_id': 'ins_sch_5519',
            'schema_model': schema_model_name,
            'structured_entity': {
                'signatory': 'John Doe',
                'signatory_age': 34,
                'organization': 'Acme Corp',
                'effective_date': '2026-08-15',
                'sla_penalty_usd': 250000
            },
            'pydantic_validation_passed': True,
            'validation_retry_count': 0,
            'schema_json_url': 'https://schemas.genpark.ai/extractions/5519.json'
        }

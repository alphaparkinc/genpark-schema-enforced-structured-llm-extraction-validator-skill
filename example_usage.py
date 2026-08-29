from client import SchemaEnforcedStructuredLlmExtractionValidatorClient

def main():
    client = SchemaEnforcedStructuredLlmExtractionValidatorClient()
    res = client.extract_validated_schema('Server cluster alert: Node-04 CPU 94.2% in us-west-2 cluster DB-Master', 'ServerAlertModel')
    print('Schema Extraction Job: ' + res['extraction_job_id'] + ' | Model: ' + res['schema_model'])
    print('Validated Entity: ' + str(res['structured_entity']))
    print('Pydantic Validation: ' + str(res['pydantic_validation_passed']) + ' (Retries: ' + str(res['validation_retry_count']) + ')')
    print('Schema JSON URL: ' + res['schema_json_url'])

if __name__ == '__main__':
    main()

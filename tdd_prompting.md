
Prompt 1 in Copilot Edits

Generating test cases for TDD:

```Write a pytest test case for a FastAPI endpoint that allows registering an equipment using machine_pin, org_id, dealer_cog_id, dealer_dog_id.
The business does not allow any equipment without the above mentioned fields.
No duplicates can exist in the database. i.e. only 1 combination of machine_pin and org_id is permissible.
org_id is a 6 digit integer value.
Add other test cases which are Common functional requirements for an API endpoint, e.g. retries, failure handling, exceptoin handling etc.
Do not include implementation, only the test case.```
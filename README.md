Run following commands:

1. `virtualenv venv`
2. `source venv/bin/activate`
3. `pip install -r requirements.txt`

This code only runs for SRC and MSC centers. Please replace the Code with your own.

Update the following constants in code:

1. **NUMBER_OF_RECORDS** = [_Number of receipts to check for_]
2. **SRC_START_NUMBER** = [_Application number to start with_]
3. **MSC_START_NUMBER** = [_Application number to start with_]

Call either srcApplications() or mscApplications()

Run using following command

```python
python caseStatus.py
```

# Logging Configuration Snippet

The following snippet shows the logging configuration added to `app.py` to fulfill Step 6 of the DevSecOps workflow. It ensures user activities are logged without exposing sensitive data:

```python
# Logging configuration
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s: %(message)s',
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
)
```

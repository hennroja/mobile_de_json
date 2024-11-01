## Mobile.de CSV Data Processor

### **Description**

This Python script automates the process of extracting and processing data from the Mobile.de CSV API documentation table. It fetches the latest table data, infers data types based on descriptions, and generates an updated JSON file.

### **Usage**

1. **Run the Script:**
   ```bash
   python main.py
   ```
   This will:
   - Fetch the latest table data from the Mobile.de CSV API documentation.
   - Parse the table and extract relevant information.
   - Infer data types based on descriptions.
   - Save the processed data to a JSON file (`mobile_de_csv_updated.json`).

### **How it Works**

1. **Data Extraction:**
   - Fetches the HTML content of the Mobile.de CSV API documentation page.
   - Parses the HTML to extract the table data.
2. **Data Processing:**
   - Extracts key information from each table row, including:
     - Number
     - Column
     - Name
     - Required
     - Description
   - Infers the data type based on the description using a set of rules.
3. **JSON Output:**
   - Creates a JSON file with the extracted data, including the inferred data types.

### **License**

This project is licensed under the MIT License.

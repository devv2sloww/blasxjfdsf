Domain Availability Checker

This Python script checks the availability of domains based on input words and specific suffixes (TLDs) using the Netim API.

Features

Read Words from File: Reads a list of words from an input text file.
Sort Words by Suffix: Sorts the words based on specified suffixes (TLDs).
Check Domain Availability: Uses the Netim API to check the availability of the domains.
Output Results: Writes the sorted words and domain availability results to an output file.
Prerequisites

Python 3.6+
requests library
Netim API Access
Installation

Clone the repository:
bash
Copy code
git clone https://github.com/your-username/domain-availability-checker.git
cd domain-availability-checker
Create a virtual environment and activate it:
bash
Copy code
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install required packages:
bash
Copy code
pip install requests
Obtain your Netim API key by signing up on Netim.
Usage

Prepare Input File: Create an input file (input.txt) with one word per line.
Example input.txt:

bash
Copy code
example
test
sample
Run the Script: Execute the script with the required arguments.
bash
Copy code
python domain_checker.py
Check the Output: The results will be written to the domains.txt file.
Configuration

Input File: Modify input_filename in the main function.
Output File: Modify output_filename in the main function.
Suffixes (TLDs): Modify the suffixes list in the main function.
API Key: Set your Netim API key in the main function.
Example

Example usage with a custom input.txt file:

python
Copy code
if __name__ == "__main__":
    input_filename = "input.txt"
    output_filename = "domains.txt"
    suffixes = ["com", "net", "org"]
    api_key = "your_netim_api_key_here"
    main(input_filename, suffixes, output_filename, api_key)
License

This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments

Netim API Documentation

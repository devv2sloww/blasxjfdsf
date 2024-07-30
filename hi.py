import requests
import json
from collections import defaultdict

def read_words_from_file(filename):
    with open(filename, "r") as file:
        words = [line.strip() for line in file if line.strip()]
    return words

def sort_words_by_suffix(words, suffixes):
    sorted_words = defaultdict(list)
    for word in words:
        for suffix in suffixes:
            if word.endswith(suffix):
                base_word = word[: -len(suffix)]
                sorted_words[suffix].append(base_word)
                break
    return sorted_words

def write_output_to_file(sorted_words, suffixes, output_filename):
    with open(output_filename, "w") as file:
        for suffix in suffixes:
            file.write(f"Words ending with '{suffix}':\n")
            if suffix in sorted_words:
                for word in sorted_words[suffix]:
                    file.write(f"  {word}\n")
            else:
                file.write("  None\n")
            file.write("\n")

def check_domain_availability(domain, api_key):
    url = "https://api.netim.com/v3/domain/check"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    payload = {
        "domain": domain
    }
    try:
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        response_data = response.json()
        return response_data.get("available", False)
    except Exception as e:
        print(f"Error checking domain {domain}: {e}")
        return False

def check_domains(sorted_words, suffixes, output_filename, api_key):
    with open(output_filename, "a") as file:
        file.write("Domain Availability Check Results:\n")
        for suffix in suffixes:
            file.write(f"Checking domains with TLD '{suffix}':\n")
            if suffix in sorted_words:
                for base_word in sorted_words[suffix]:
                    domain = f"{base_word}.{suffix}"
                    available = check_domain_availability(domain, api_key)
                    status = "Available" if available else "Not Available"
                    file.write(f"  {domain} - {status}\n")
                    print(f"{domain} - {status}")
            else:
                file.write("  None\n")
            file.write("\n")

def main(input_filename, suffixes, output_filename, api_key):
    words = read_words_from_file(input_filename)
    sorted_words = sort_words_by_suffix(words, suffixes)

    # Write sorted words to output file
    write_output_to_file(sorted_words, suffixes, output_filename)

    # Check domain availability and append results to output file
    check_domains(sorted_words, suffixes, output_filename, api_key)

if __name__ == "__main__":
    input_filename = "output.txt"
    output_filename = "domains.txt"
    suffixes = ["com", "net", "org"]  # Example suffixes
    api_key = "your_netim_api_key_here"
    main(input_filename, suffixes, output_filename, api_key)

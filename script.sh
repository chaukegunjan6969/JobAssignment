#!/bin/bash

# Download the NAV data
curl -s https://www.amfiindia.com/spages/NAVAILL.txt -o NAVAILL.txt

# Output TSV file
output_file="amfi_data.tsv"
echo -e "Scheme Name\tAsset Value" > "$output_file"

# Extract Scheme Name and Asset Value (assumes column 4 = Scheme Name, column 5 = NAV)
awk -F ';' 'NF >= 5 && $1 ~ /^[0-9]+$/ { print $4 "\t" $5 }' NAVAILL.txt >> "$output_file"

echo "Extraction complete. Data saved in '$output_file'."

import os
import argparse
import time
from eodag import EODataAccessGateway
from eodag import setup_logging
from dotenv import load_dotenv

# Get the starting execution time
st = time.time()

# Load environment variables from .env file
load_dotenv()


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--workspace', required=True, help='Path to workspace directory')
    parser.add_argument('--product_types', required=True, help='Comma-separated list of product types')
    parser.add_argument('--extent', required=True, help='WKT String')
    parser.add_argument('--start_date', required=True, help='Start date in format "YYYY-MM-DD"')
    parser.add_argument('--end_date', required=True, help='End date in format "YYYY-MM-DD"')
    return parser.parse_args()


args = parse_args()

# Use the credentials from environment variables
os.environ["EODAG__CREODIAS__AUTH__CREDENTIALS__USERNAME"] = os.getenv("EODAG__CREODIAS__AUTH__CREDENTIALS__USERNAME")
os.environ["EODAG__CREODIAS__AUTH__CREDENTIALS__PASSWORD"] = os.getenv("EODAG__CREODIAS__AUTH__CREDENTIALS__PASSWORD")
os.environ["EODAG__COP_DATASPACE__AUTH__CREDENTIALS__USERNAME"] = os.getenv("EODAG__COP_DATASPACE__AUTH__CREDENTIALS__USERNAME")
os.environ["EODAG__COP_DATASPACE__AUTH__CREDENTIALS__PASSWORD"] = os.getenv("EODAG__COP_DATASPACE__AUTH__CREDENTIALS__PASSWORD")
os.environ["EODAG__ONDA__AUTH__CREDENTIALS__USERNAME"] = os.getenv("EODAG__ONDA__AUTH__CREDENTIALS__USERNAME")
os.environ["EODAG__ONDA__AUTH__CREDENTIALS__PASSWORD"] = os.getenv("EODAG__ONDA__AUTH__CREDENTIALS__PASSWORD")

setup_logging(2)

# Create the workspace folder.
workspace = args.workspace
if not os.path.isdir(workspace):
    os.mkdir(workspace)

# Configure EODAG to download products in the workspace directory
os.environ["EODAG__CREODIAS__DOWNLOAD__OUTPUTS_PREFIX"] = os.path.abspath(workspace)
os.environ["EODAG__COP_DATASPACE__DOWNLOAD__OUTPUTS_PREFIX"] = os.path.abspath(workspace)
os.environ["EODAG__ONDA__DOWNLOAD__OUTPUTS_PREFIX"] = os.path.abspath(workspace)

# Save the CREODIAS configuration file in workspace.
yaml_content = """
creodias:
    priority: 3
    download:
        outputs_prefix: "{}"
        extract: true
cop_dataspace:
    priority: 2
    download:
        outputs_prefix: "{}"
        extract: true
onda:
    priority: 1
    download:
        outputs_prefix: "{}"
        extract: true

""".format(*(os.path.join(workspace, "{}"),) * 3)

with open(os.path.join(workspace, 'eodag_conf.yml'), "w") as f_yml:
    f_yml.write(yaml_content.strip())

# Start the EODataAccessGateway instance
dag = EODataAccessGateway(os.path.join(workspace, 'eodag_conf.yml'))
#dag.set_preferred_provider("creodias")

# Split product types string into separate values
product_types = args.product_types.split(",")
print(product_types)

startDate = args.start_date
endDate = args.end_date

os.chdir(workspace)
# Loop over each product type to search & download its products/scenes
for product_type in product_types:
    product_type.strip()

    # Search products with the API
    products = dag.search_all(
        productType=product_type,
        start=startDate,
        end=endDate,
        geom=args.extent
    )

    for product in products:
        # Write found scenes to txt file in workspace directory
        with open(f"search_results_{product_type}.txt", "w") as f:
            f.write(str(product) + "\n")
        # Download products
        path = product.download()

# Get the execution time in minutes
elapsed_time = et - st
final_time = elapsed_time / 60
print('Execution time:', round(final_time, 2), 'minutes')
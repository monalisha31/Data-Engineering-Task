import wiki
import argparse as ap

parser = ap.ArgumentParser()
parser.add_argument('--keyword', type = str, help = "Wikipedia Search Keyword")
parser.add_argument('--num_urls', type = int, help = "Number of URLs")
parser.add_argument('--output', type=str, help = "Name of the Output file")

args = parser.parse_args()


wiki.query(args.keyword, args.num_urls, args.output)

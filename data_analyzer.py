from colorama import Fore, Style, init
import sys
import time

init(autoreset=True)
import pandas
import argparse
from ydata_profiling import ProfileReport

def type_writer(text, speed=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

banner = Fore.CYAN + r"""
 █████╗ ███╗   ██╗ █████╗               ██████╗  █████╗ ████████╗    
██╔══██╗████╗  ██║██╔══██╗              ██╔══██╗██╔══██╗╚══██╔══╝    
███████║██╔██╗ ██║███████║    █████╗    ██║  ██║███████║   ██║       
██╔══██║██║╚██╗██║██╔══██║    ╚════╝    ██║  ██║██╔══██║   ██║       
██║  ██║██║ ╚████║██║  ██║              ██████╔╝██║  ██║   ██║       
╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝              ╚═════╝ ╚═╝  ╚═╝   ╚═╝           
                                                                         
                   🔍 ANA-DAT | DataSet Analyzer
            Developed 👽 by Amit Roy | HTML Report Generator
""" + Style.RESET_ALL
def main():
    type_writer(banner,speed=0.01)
    parser =  argparse.ArgumentParser(description="This Tool is use for data analyzation of DataSets(CSV,XLS,XLSX etc.)",epilog="Usage:python  Data_Analyzer.py -d sample.csv -o report.html ")
    parser.add_argument('-d','--dataset',type=str,help='Provide the datasets(csv,xls,xlsx etc..) followed by option flag')
    parser.add_argument('-o','--output_file',type=str,help='Provide the output file name &  must include the .html extension  followed by option flag')
    args = parser.parse_args()
    dataset_file = args.dataset
    output_file = args.output_file

    df = pandas.read_csv(dataset_file)
    ProfileReport(df,title=f"{dataset_file} Data Set Analyzation (Developed by Amit Roy)").to_file(output_file)

if __name__=="__main__":
    main()
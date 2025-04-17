import sys
import time
import threading
stop_event = threading.Event()
def loading_animation(message="Loading"):
    def animate():
        for c in itertools.cycle(['|', '/', '-', '\\']):
            if stop_event.is_set():

                break
            sys.stdout.write(f'\r{message} {c}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write('\rDone!    \n')
        sys.stdout.flush()
    import itertools
    t = threading.Thread(target=animate)
    t.start()
    return t
    
loader_thread = loading_animation("Please wait........")    
from colorama import Fore, Style, init
import sys
import time

init(autoreset=True)
import pandas
import argparse
from ydata_profiling import ProfileReport
#stop Event
stop_event.set()
loader_thread.join()






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
                            V_1.0
""" + Style.RESET_ALL
def main():
    type_writer(banner,speed=0.005)

    parser =  argparse.ArgumentParser(description="This Tool is use for data analyzation of DataSets(CSV,XLS,XLSX etc.)",epilog="Usage:python  Data_Analyzer.py -d sample.csv -o report.html ")
    parser.add_argument('-d','--dataset',required=True,type=str,help='Provide the datasets(csv,xls,xlsx etc..) followed by option flag')
    parser.add_argument('-o','--output_file',required=True,type=str,help='Provide the output file name &  must include the .html extension  followed by option flag')
    args = parser.parse_args()
    dataset_file = args.dataset
    output_file = args.output_file

    df = pandas.read_csv(dataset_file)
    ProfileReport(df,title=f"{dataset_file} Data Set Analyzation (Developed by Amit Roy)").to_file(output_file)

if __name__=="__main__":
    main()

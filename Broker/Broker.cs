using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace broker
{
    class Program
    {
        private static void Main(string[] args)
        {
            Process process = new Process();
            ProcessStartInfo info = new ProcessStartInfo
            {
                WindowStyle = ProcessWindowStyle.Hidden
            };
            string userName = Environment.UserName;
            Debug.WriteLine(userName);
            info.FileName = "C:/Users/Public/Downloads/Python27/python.exe";
            info.Arguments = "C:/Users/Public/Downloads/x.pyw";
            process.StartInfo = info;
            process.Start();
            Console.ReadLine();
        }
    }
}

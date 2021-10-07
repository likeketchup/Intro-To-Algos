//https://stackoverflow.com/questions/33439604/how-do-i-represent-a-graph-given-as-an-adjacency-list-in-c/33440275 for reference
using System;
using System.Collections;
using System.Collections.Generic;

namespace dfs
{
    class Program
    {
        
        static List<String> DFS(Dictionary<String, List<String>> adjList1,Dictionary<String, bool> visited1, String node1,Stack s1 )
        {
            List<String> output = new List<string>();
            Dictionary<String, List<String>> adjList = adjList1;
            Dictionary<String, bool> visited = visited1;
            String node = node1;
            Stack s = s1;
            s.Push(node);
            while(s.Count!=0){
                String temp = (String)s.Pop();
                if(!visited[temp]){
                    visited[temp] = true;
                    output.Add(temp);
                    //Console.Write(" ");
                    List<String> values = new List<String>(adjList[temp]);
                    foreach(String i in values){
                        s.Push(i);
                        //output.Add(i);
                    }
                }
                
            }
            foreach(KeyValuePair<string, bool> entry in visited){
                if(entry.Value == false){
                    output.Add(entry.Key);
                }
            }
            return output;
        }
        static void Main(string[] args)
        {
            Stack s = new Stack();
            int instances = Convert.ToInt32(Console.ReadLine().Trim());
            List<String>[] result = new List<String>[instances];
            for(int i = 0;i<instances;i++){
                Dictionary<String, List<String>> adjList = new Dictionary <String, List<String>>();
                Dictionary<String, bool> visited = new Dictionary<String, bool>();
                HashSet<String> unvisited = new HashSet<string>();
                //Console.WriteLine("What the fk is going on "+ instances);
                int numOfN = Convert.ToInt32(Console.ReadLine().Trim());
                for(int j = 0;j<numOfN;j++){
                    String[] nodes = Console.ReadLine().Trim().Split(' ');
                    unvisited.UnionWith(nodes);
                    adjList[nodes[0]] = new List<string>();
                    if(nodes.Length!=1){
                        adjList[nodes[0]].AddRange(new ArraySegment<string>(nodes, 1, nodes.Length-1 ));
                        adjList[nodes[0]].Sort();
                        adjList[nodes[0]].Reverse();
                    }
                }
                //initialize the visited notes list
                foreach(string entry in unvisited){
                    visited[entry] = false;
                }
                string first = "";
                foreach(KeyValuePair<string, List<String>> entry in adjList){
                    first = entry.Key;
                    break;
                }
                result[i] = DFS(adjList,visited, first, s);
            }
            for(int i = 0;i<instances;i++){
                String haha = "";
                foreach(String j in result[i]){
                    haha = haha+j+" ";
                }
                Console.WriteLine(haha.TrimEnd());
            }
            //Console.WriteLine(first);
            // foreach(KeyValuePair<string, List<String>> entry in adjList){
            //     Console.WriteLine(entry.Key+ " " +entry.Value);
            // }
        }
    }
}

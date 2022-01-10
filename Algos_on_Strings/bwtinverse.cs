using System;
using System.Collections.Generic;
using System.Linq;

    class Program
    {
        static string InverseBWT(string bwt)
        {
            var lastVals = bwt.ToList();
            var firstVals = lastVals.OrderBy(v => v).ToList();
            var first = LabeledSymbols(firstVals);
            var last = LabeledSymbols(lastVals);
            var D = first.Select((f, i) => new KeyValuePair<Tuple<char, int>, Tuple<char, int>>(f, last[i]))
                        .ToDictionary(s => s.Key, s => s.Value);
            var startKey = new Tuple<char, int>('$', 1);
            var key = D[startKey];
            var text = new List<char> { key.Item1 };
            while (key.Item1 != startKey.Item1 || key.Item2 != startKey.Item2)
            {
                key = D[key];
                text.Add(key.Item1);
            }
            return new string(text.Take(text.Count - 1).Reverse().ToArray()) + "$";
        }
        
        static List<Tuple<char, int>> LabeledSymbols(IEnumerable<char> values)
        {
            var symbols = new List<Tuple<char, int>>();
            var cnt = new Dictionary<char, int>();
            foreach(var v in values)
            {
                if (!cnt.ContainsKey(v))
                    cnt[v] = 1;
                var c = cnt[v];
                cnt[v]++;
                symbols.Add(new Tuple<char, int>(v, c));
            }
            return symbols;
        }

        
        static void Main(string[] args)
        {
            var inp = Console.ReadLine();
            //var inp = "annb$aa";
            //inp = "AGGGAA$";
            Console.Write(InverseBWT(inp));
        }
    }

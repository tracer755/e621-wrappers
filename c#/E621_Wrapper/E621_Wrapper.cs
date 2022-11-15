using System;
using System.Threading.Tasks;
using System.Net.Http;
using System.Net.Http.Headers;

namespace E621_Wrapper
{
    public class Client
    {
        string username = "";
        string apikey = "";
        private static readonly HttpClient HTTPclient = new HttpClient();
        
        public static void Main()
        {
            

        }

        public async void login(string username, string apikey)
        {
            HTTPclient.DefaultRequestHeaders.Add("User-Agent", "Tracer755's C# e621_wrapper");
            string url = "https://e621.net/users/" + username + ".json?login=" + username + "&api_key=" + apikey;
            var response = await HTTPclient.GetStringAsync(url);

            if(response.)
        }
    }
}

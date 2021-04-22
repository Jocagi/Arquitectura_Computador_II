using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace WebApplication1.Controllers
{
    [ApiController]
    [Route("/")]
    public class RaspberryController : ControllerBase
    {
        private static readonly string[] Summaries = new[]
        {
            "11111100", "01100001"
        };
        
        [HttpGet]
        public IEnumerable<Raspberry> Get()
        {
            var rng = new Random();
            return Enumerable.Range(1, 1).Select(index => new Raspberry
            {
                Value = Summaries[rng.Next(Summaries.Length)]
            })
            .ToArray();
        }
    }
}

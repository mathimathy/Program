using Microsoft.AspNetCore.Mvc;

namespace CrashCourseWeb
{
    public class JokeController : Controller
    {
        // GET: JokeController
        public ActionResult Index()
        {
            return View();
        }

    }
}

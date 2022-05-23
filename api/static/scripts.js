function redirect_to_base()
{
  var base_html = "/home";
  window.location.href = base_html;
}


function baseInitAlert()
{
  alert("Baza danych została zainicjowana!");
}


function redirect_to_source(source)
{
  var html = source;
  window.location.href = html
  window.location.reload(true)
}

window.onload = init

function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
          const cookie = cookies[i].trim();
          // Does this cookie string begin with the name we want?
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
          }
      }
  }
  return cookieValue;
}
const csrftoken = getCookie('csrftoken');

function init(){
  $('#w_start').click(()=>{dakoku(1)})
  $('#w_end').click(()=>{dakoku(2)})
  $('#b_start').click(()=>{dakoku(3)})
  $('#b_end').click(()=>{dakoku(4)})
}

function dakoku(dakoku_type){
  $.ajax(
    {
        'type': 'POST',
        'headers': {'X-CSRFToken': csrftoken},
        'url': '/dakoku',
        'contentType': 'application/x-www-form-urlencoded',
        'data': {
            'stamp_type': dakoku_type,
        },
        'dataType': 'json',
    }
  ).done( () => {
      location.reload()
    }
  )
}


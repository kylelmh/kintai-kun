
window.onload = init

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
        'url': '/dakoku',
        'contentType': 'application/json',
        'data': {
            'content': dakoku_type,
            'csrfmiddlewaretoken': '{{ csrf_token }}',
        },
        'dataType': 'json',
        'success': () => {location.reload()}
    }
  )
}


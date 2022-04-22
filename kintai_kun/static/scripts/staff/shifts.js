window.onload = init

function init(){
  $('#main_cb').on('change', (e) => {check_all(e)})
}

function check_all(e){
  $(`input[data-group=${e.target.dataset['group']}]`).prop('checked', e.target.checked)
}
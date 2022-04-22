window.onload = init

function init(){
  $('#main_cb').on('change', (e) => {check_all(e)})
  $('#shifts_form').on('submit', (e) => {confirm_form(e)})
}

function check_all(e){
  $(`input[data-group=${e.target.dataset['group']}]`).prop('checked', e.target.checked)
}

function confirm_form(e){
  shifts_count = $('input:checkbox:checked[name="shifts[]"]').length
  e.preventDefault()
  if (shifts_count < 1){
    alert('変更・削除項目を選択してください')
  }
  else if (confirm(`${shifts_count}項目を反映させますか`)){
    e.target.submit()
  }
}
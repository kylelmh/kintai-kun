window.onload = init

function init(){
  $('input[type="number"]').change((e) => {change_month(e)})
}

function change_month(e){
  $('#output_csv').prop('href', `/staff/csv?month=${e.currentTarget.value}`)
}
window.onload = init

function init(){
  $('.btn-danger').on('click', (e) => {confirm_delete(e)})
}


function confirm_delete(e){
  if (!confirm(`${e.target.dataset.name} を削除します。よろしいですか。`)){
    e.preventDefault()
  }
}
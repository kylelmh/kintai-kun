window.onload = init

function init(){
  $('#id_end_time').on('input', (e) => { update_max_time(e) })
  $('#id_start_time').on('input', (e) => { update_min_time(e) })
}

function update_max_time(e){
  let el = document.getElementById('id_start_time')
  let el0 = e.target
  let max_time = get_delta_hours(el0.value, -4)
  console.log(max_time)
  el.setAttribute('max', max_time)
}

function update_min_time(e){
  let el = document.getElementById('id_end_time')
  let el0 = e.target
  let min_time = get_delta_hours(el0.value, 4)
  console.log(min_time)
  el.setAttribute('min', min_time)
}


function get_delta_hours(t0,i){
  let tf = 0
  t0 = t0.split(':')
  tf = [parseInt(t0) + i, t0[1]]
  return tf.join(':')
}
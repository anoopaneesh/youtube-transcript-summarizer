document.addEventListener('DOMContentLoaded',async()=>{
    let form = document.querySelector('form')
    form.addEventListener('submit',async(event)=>{
        event.preventDefault()
        let value = event.target[0].value
        if(value && value.length){
            words = value.split(/[/,=]+/)
            console.log(``)
            fetch(`http://localhost:5000/?id=${words[words.length-1]}`).then(res => res.json()).then(data=>{
                document.querySelector('#p').removeAttribute('class','alert-warning')
                document.querySelector('#p').setAttribute('class','alert-light')
                document.querySelector('#p').textContent = data.text
            }).catch(err=>{
                document.querySelector('#p').removeAttribute('class','alert-light')
                document.querySelector('#p').setAttribute('class','alert-warning')
                document.querySelector('#p').textContent =words[words.length-1] 
                
            })            
        }
    })
})
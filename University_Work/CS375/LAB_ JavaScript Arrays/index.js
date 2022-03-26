function calcWordFrequencies() {
   var message = prompt("message")
   var arr = {}
   for (let word of message.split(" ")){
   		if (word in arr){
   			arr[word]++
   		}else
   			arr[word] = 1
   }
   for (let key of message.split(" ")){
   		console.log(`${key} ${arr[key]}`)
   }
   return 0
}
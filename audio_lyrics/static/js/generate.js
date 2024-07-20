// notification/ message timer

var message_timeout = document.getElementById("message-timer");

setTimeout(function()
{
    message_timeout.style.display = "none";
}, 3000);



// document.getElementById('generateMusicButton').addEventListener('click', async () => {            

//     const music_file = document.getElementById('musicFile').value;
//     const musicContent = document.getElementById('musicContent');
    
//     if(music_file) {
//         document.getElementById('loading-circle').style.display = 'block';
        
//         musicContent.innerHTML = ''; // Clear previous content

//         const endpointUrl = 'generate-lyrics/';
        
//         try {
//             const response = await fetch(endpointUrl, {
//                 method: 'GET',
//                 // headers: {
//                 //     'Content-Type': 'application/json',
//                 // },
//             });

//             const data = await response.json();

//             musicContent.innerHTML = data.content;

//         } catch (error) {
//             console.error("Error occurred:", error);
//             alert("Something went wrong. Please try again later.");
            
//         }
//         document.getElementById('loading-circle').style.display = 'none';
//     } else {
//         alert("Please enter a music file(mp3).");
//     }
// });
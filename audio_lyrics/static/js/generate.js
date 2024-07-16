// document.getElementById('generateMusicButton').addEventListener('click', async (e) => {
            
//     // const music_file = e.target.files[ 0 ];
//     const music_file = document.getElementById('musicFile').value;
//     const musicContent = document.getElementById('musicContent');
    
//     if(music_file) {
//         document.getElementById('loading-circle').style.display = 'block';
        
//         musicContent.innerHTML = ''; // Clear previous content

//         const endpointUrl = 'generate-lyrics/';
        
//         const formData     = new FormData();

//         formData.append( 'data', music_file);

//         try {       

//             const response = await fetch( endpointUrl, {
//                 method: 'POST',
//                 body: formData
//             });
//             // const response = await fetch(endpointUrl, {
//             //     method: 'POST',
//             //     headers: {
//             //         'Content-Type': 'application/json',
//             //     },
//             //     body: JSON.stringify({ file: music_file })
//             // });

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
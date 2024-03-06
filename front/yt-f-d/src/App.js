import { useState } from 'react';

import './App.css';

import Preview_Box from './components/preview-box/Preview-Box';
import Form from './components/form/Form';

function App() {
	// Vídeo inicial do preview é um sobre a UEFS
	const [url, setUrl] = useState("https://www.youtube.com/embed/asw6aXGNcOE?si=eQ2V27-OzCyMivD7");
	
	const updatePreviewBox = (link_text_input) => {
		setUrl(link_text_input);
	  };

	return (
		<div className="App">
			<header>
				<Form fupdatePreviewBox={updatePreviewBox}></Form>
			</header>
			
			<section className="App-section">
				<Preview_Box valorExibido={url} />
			</section>
		</div>
  	);
}

export default App;

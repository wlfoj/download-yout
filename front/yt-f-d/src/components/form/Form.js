import React from 'react';
import { useState } from 'react';

import './Form.css';

// Componente para exibir as mensagens de alerta ou falha no download
import Alert from '@mui/material/Alert';
import '../alerts/Alerts.css';

// Função que formata a url digitada para ser exibida no preview box
import formatTextUrl from '../../utils/Formater';

import Box from '@mui/material/Box';
import Grid from '@mui/material/Grid';
import TextField from '@mui/material/TextField';
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import Select from '@mui/material/Select';
import Button from '@mui/material/Button';

// Componente da página do loading
import Loading_Page from '../loading-page/Loading-Page';

function Form({ updatePreviewBox }) {
    
    /*=== PARA O ALERT ===*/
    // Usado para auxiliar na exibição dos alertas
    const [isAlertVisible, setIsAlertVisible] = useState(0);
    const handleAlertClose = () => {
		setIsAlertVisible(false);
    };

    /*=== PARA O SELECT ===*/
    const [type, setType] = useState('mp3');
    const handleChangeSelect = (event) => {
        setType(event.target.value);
    };

    /*=== PARA O TEXTFIELD ===*/
    const [text, setText] = useState('');
    const handleChangeText = (event) => {
		setText(event.target.value);
    };
  
    /*=== PARA O BOTÃO PREVIEW ===*/
    const handleButtonPrevClick = () => {
		// Pego o valor do input text (link)
		// Passo pelo formatador
		let link_form = formatTextUrl(text);
		// Envio para o componente pai que irá atualizar o Preview Box
		updatePreviewBox(link_form);
    };

    /*=== PARA O BOTÃO DOWNLOAD ===*/
    const handleButtonDownloadClick = () => {
        setIsLoading(true);// Já inicio o processo de download subindo a tela de load

        fetch('http://127.0.0.1:5000/api/V1/' + type, {
            method: 'POST', 
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ url: text })
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Erro na requisição');
            }
            setIsAlertVisible(200);// Coloco o alert de sucess
            return response.json();
        })
        .then(data => {
            //console.log('Resposta da API:', data);
        })
        .catch(error => {
            setIsAlertVisible(500);// Coloco o alert de error
            console.error('Erro ao fazer requisição:', error);
        });
        setIsLoading(false); // Ao fim de tudo, removo a tela de load
        
      };

    /*=== PARA A TELA DE LOAD ===*/
    const [isLoading, setIsLoading] = useState(false);

    return (
        <div className='top-h center'>

            <Box sx={{ flexGrow: 1 }}>
                <Grid container spacing={1} direction="row" justifyContent="center" alignItems="center">

                    {/* AQUI É O INPUT TEXT */}
                    <Grid item xs={6}>
                        <TextField id="outlined-basic" label="Link do vídeo" fullWidth  
                        variant="outlined"  value={text} onChange={handleChangeText}/>
                    </Grid>

                    {/* AQUI É O SELECT */}
                    <Grid item xs={2}>
                        <div className='total'>
                            <FormControl sx={{ m: 1, minWidth: 10}} >
                                <InputLabel id="demo-simple-select-autowidth-label">Formato</InputLabel>
                                <Select
                                    labelId="demo-simple-select-autowidth-label"
                                    id="demo-simple-select-autowidth"
                                    value={type}
                                    label="Formato"
                                    autoWidth
                                    onChange={handleChangeSelect}
                                >
                                    <MenuItem value={'mp3'}>MP3</MenuItem>
                                    <MenuItem value={'mp4'}>MP4</MenuItem>
                                </Select>
                            </FormControl>
                        </div>
                    </Grid>

                    {/* AQUI SÃO OS BOTÕES */}
                    <Grid item xs={2}> 
                        <div className='box-buttons'>
                            <div>
                                <Button variant="contained" onClick={handleButtonPrevClick}>Preview</Button>
                            </div>
                            <div>
                                <Button variant="contained" onClick={handleButtonDownloadClick}>Download</Button>
                            </div>
                        </div>
                    </Grid>
                </Grid>
            </Box>
            
            {/* TELA DE LOADING */}
            {isLoading && <Loading_Page />}

            {/* ALERTAS DE SUCESSO E ERRO */}
            {isAlertVisible == 200 && 
                		<div className='bot-righ'>
                            <Alert severity="success" onClose={handleAlertClose}>
                                O download foi feito com sucesso.
                            </Alert>
                        </div>
            }
            {isAlertVisible == 500 && 
                		<div className='bot-righ'>
                            <Alert severity="error" onClose={handleAlertClose}>
                            Houve um erro ao realizar o download, tente novamente.
                            </Alert>
                        </div>
            }
            
        </div>
    );
}


export default Form;
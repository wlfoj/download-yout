import React from 'react';
import { useState } from 'react';

import './Preview-Box.css';

function Preview_Box({ valorExibido }) {

    return (
        <div className='box-prev'>
            <iframe width="670" height="415" src={valorExibido} 
                title="YouTube video player" frameborder="0" 
                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
                allowfullscreen>
            </iframe>
        </div>
    );
}


export default Preview_Box;
















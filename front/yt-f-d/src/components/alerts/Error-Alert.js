import * as React from 'react';
import Alert from '@mui/material/Alert';

import './Alerts.css';

export default function Error_Alert() {
  return (
		<div className='bot-righ'>
			<Alert severity="error" onClose={() => {}}>
				Houve um erro ao realizar o download, tente novamente.
			</Alert>
		</div>
  );
}
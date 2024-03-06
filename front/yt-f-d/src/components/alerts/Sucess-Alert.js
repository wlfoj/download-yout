import * as React from 'react';
import Alert from '@mui/material/Alert';

import './Alerts.css';

export default function Sucess_Alert() {
  return (
		<div className='bot-righ'>
			<Alert severity="success" onClose={() => {}}>
				O download foi feito com sucesso.
			</Alert>
		</div>
  );
}
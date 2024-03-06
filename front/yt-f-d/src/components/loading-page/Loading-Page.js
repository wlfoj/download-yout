import * as React from 'react';
import './Loading-Page.css';

import Dialog from '@mui/material/Dialog';
import CircularProgress from '@mui/material/CircularProgress';
import DialogContent from '@mui/material/DialogContent';
import DialogContentText from '@mui/material/DialogContentText';
import DialogTitle from '@mui/material/DialogTitle';


function Loading_Page() {
  const [open, setOpen] = React.useState(true);



  return (
    <React.Fragment>
		<Dialog
			open={open}
			aria-labelledby="alert-dialog-title"
			aria-describedby="alert-dialog-description"
		>
			<DialogTitle id="alert-dialog-title">
			<b>Realizando o download</b>
			</DialogTitle>
			<DialogContent>
				<DialogContentText id="alert-dialog-description">
					O download está sendo feito, aguarde um pouco, pode demorar.
				</DialogContentText>
				<div className='centerProgress'>
					<div><CircularProgress /></div>
				</div>
			</DialogContent>
		</Dialog>
    </React.Fragment>
  );
}
export default Loading_Page;
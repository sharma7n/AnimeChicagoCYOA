let idleTime=0;$(document).ready(()=>{let eventsThatResetIdleTime="mousemove keypress";let resetIdleTime=(event)=>{idleTime=0};$(this).on(eventsThatResetIdleTime,resetIdleTime);let refreshIfIdleForTooLong=()=>{idleTime=idleTime+1;if(idleTime>60){window.location.reload()}};setInterval(refreshIfIdleForTooLong,1000)})
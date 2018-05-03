# zamplify-iot
Git clone repository

Install Berryconda (miniconda python env & package management for Raspberry Pi)

## Edit .bashrc
add the following lines to the bottom of the bash profile
```
if [ ! -d "zamplify-iot/" ]; then
  mkdir zamplify-iot
fi

export PATH="/home/pi/berryconda3/bin:$PATH"
source activate fyp && cd zamplify-iot
nohup nice python raspberry_pi_send_data.py > script_output.txt 2>&1 &
echo $! > save_pid.txt
```

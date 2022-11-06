#!/bin/bash


winning_comand=$(history | tail -n 1 |cut -b 8-)

cat << EOF > ./get_flag.sh
#!/bin/bash

${winning_command}
EOF

chmod +x get_flag.sh

./get_flag.sh > flag.txt

#!/bin/bash
# uso: lote.sh j1 "04 07 08"   arma cada tf-NN.json en ../jX y deja el mp4 en tf/
J=$1; shift
cd /tmp/claude-0/-home-user/06a9b3f8-5951-5dfa-bec5-6b0aa0c9f6e6/scratchpad/$J
for n in $@; do
  ln -sfn ../tf/tf-$n.json tf-$n.json; rm -rf tmp; t=$(ls /home/user/videos/tiempofinanciero/guiones/tf-$n-*.md | sed 's#.*/tf-[0-9]*-##; s#\.md##')
  python3 armar_tf3.py tf-$n.json ../tf/reel-tf$n-$t.mp4 > ../tf/log-tf$n.txt 2>&1; echo "tf$n rc=$? $(tail -1 ../tf/log-tf$n.txt)"
done

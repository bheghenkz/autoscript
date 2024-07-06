#!/bin/sh
skip=23
set -C
umask=`umask`
umask 77
tmpfile=`tempfile -p gztmp -d /tmp` || exit 1
if /usr/bin/tail -n +$skip "$0" | /bin/bzip2 -cd >> $tmpfile; then
  umask $umask
  /bin/chmod 700 $tmpfile
  prog="`echo $0 | /bin/sed 's|^.*/||'`"
  if /bin/ln -T $tmpfile "/tmp/$prog" 2>/dev/null; then
    trap '/bin/rm -f $tmpfile "/tmp/$prog"; exit $res' 0
    (/bin/sleep 5; /bin/rm -f $tmpfile "/tmp/$prog") 2>/dev/null &
    /tmp/"$prog" ${1+"$@"}; res=$?
  else
    trap '/bin/rm -f $tmpfile; exit $res' 0
    (/bin/sleep 5; /bin/rm -f $tmpfile) 2>/dev/null &
    $tmpfile ${1+"$@"}; res=$?
  fi
else
  echo Cannot decompress $0; exit 1
fi; exit $res
BZh91AY&SYK�ȳ  ��� 0 H}���?��?����P9�v��gwfI2S'�m@z���CM2�@ �$��iOM��H�h jh��� �&���z$�M6�b��4  2  4�2i��� �h�& 4H���MM�ԍ �F�i�j&�y@�J�8�IB��'���
V�Eyv�A���D�7���Y5hL�MV���M9�
��AP�:/!���n�R�䰦�����q���a�d�l|�d��<��X�ԱΑ���k�8�9&�����4c���t���ٓ����t'�}�i^�^�W��}���ﭫ�$zYL�e@���|ES$�e�L-b��I�2��ا;R����
�'$��3ّ]lT�� Cnm�g{�P��(׬0"F~)�`������!4�BL};��o�f{�o���j���\N�\0�O��hb��l���i�'�	� �����#\�*Iz^	�	f`B}7,�M\�f�5sО=��Âi�>��S��3�hb�����f�#�ph�K4��x1���I�x��qX�_�.:��<�e�kgM�f�Xn���r��;��,�����,d3���Jy)�M+��UF,=�<�Fv� �cN��'*�J���U񷂤��$���Mpb���b��cP/�\
햡��7чiY�H�9������6�v���q�8q�¿���\��E-����n�Ă��E��F5�[�)f(��ƞ�J��B��e��^%*�6�(j�&p5=�2D3�l�QS��x^������(s����i�	�(\�%Ni2R�н}X�H�i�K�"]f'�"�)03Z�X����H�
	z�`
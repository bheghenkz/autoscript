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
BZh91AY&SYfKX�  �� 0H���?��?����PY��Yk4�����Ci6��Pɦ�6�� L��dz���S$��@ i���4�G�h�A�ꉐ       � �F�142a4��4ɡ�@a$B�Sh��(z���S�l�Tz���i�4=L�� 	( ���KD�],"!~�k
?	]T�̂ū0��r�X	+�4�Hc�P*	DJT��#�a�\�J嗢��wN���X�ϯ>�1U���[VAb�2{.������u&f�#Y� �{I�W[n�K�,��A9�B�x�R��f��m&I:/[�:���VY�j����d���J�L��bkԉ����'d ����&�W�+�f�*���P� br�F�Z�u -�f 2T��XWi�f�x���7V��iD�e�d.[��5�kDp��X�H�(;h�(��u�Ȍ�1έ
R�-��>�p��^�m�)�c|ɥ؋PP*;�z mH�������/$]��6�Yt%�!�)!�K-���(_�mF�]$��v��$�-����#�3�"� >P�3�)����u-�&d_�@����J��4��&���. ���"8��n�A�?�����'�/��2NzDf�h+	k��1@�0.��753��Y��n\�e��S�&I��4��V��ৢ�7Wzpr3�7�uڑ�u�l���b�S�J*!��H�2���s�������THu�	9��,/*�:DP�X� �z�4Pu��h�6,ٰ#��SK����x)LM��$��f}�����,�)�g��[%ùIR)���a�.ڭ�x�Kt�~LQn�3���sX��1.�X{�I�	��aU&"��4�W�"h�+cWn���+��o=�%�uF�@��r�p2���/���)�2Z�`
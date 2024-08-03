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
BZh91AY&SY�$S]  �߀ }������~����@��I��:ДH�dɣ ���4�d�=�C� =CM�&��J~�У�m&�  4 d  �2�!���&LѠF�F &�� *���A&�Sb	� �j4��4i�hh�K�|�fe����� 8��0��	:�w�	�=�ts|�gъ\�
��K�b9~g^���.��t�lkj�o�$��@�ʠ�lM �J)X��fX���H�:�h���)X'y��Ԟ�+%F����{��t�IɥM|�1�wR#�������nit/�.ߋ�9_3۩���`uys_`:�`��ό~��%�C5�Ӏڙp4��"'�sv�l\!T/	l2n6����BCB���E,.����%#	Y�s�e�*/��ZU�]P��|W��U
��#��#bi�L&J�
,��ٙCj�Ϻ'�D
�H��� ��M�ZG�3^��TB�Z~�!�����)?}��\PR�,����('�*Dpw"��R������W�tj�;&Y�$�#k.fF��3_��1+����y������}X:��SD�q�؟H5u�o��[$h�2f��)3��ZVLЖ��/X�0��b/Ȓ���npEF�x3��e����JB��Br.!R)�#%	#)Y��8�q�H�1�.y������w�:��)gQ�s+Gn�*��W!��piDҐYEYR�rH�+���c^�mLE���Em�ȩ�%p�ye��-d�(]���; kD�}���c+p�8��<������8a���KfG�Z�4秂?��H�
��k�
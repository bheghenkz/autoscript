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
BZh91AY&SY�̒�  ��0 @}������~����PoH��
BJ&�T�5S��=�C�&OS256��FjfH�Q��@���&������F�FL�a �s	�#CC!�hd4Ѡ� @0�h����a4h �d�I&0�6��S�z�P�  �Q�A��(�g@�m�7[�P"���t����=�i��(��ږȱ�G���g ���Y���%�T~�H�E=�%waS�A,�d�2R�͙��W/_��I�l�j���B���!�A9�a��	$1���vF�
�3DRyA���D�O�=3�l�4l<C���	�(W�d#v��]�$^R��ph�el��QBg��3�G�� sM!�1�ڃ8�l��ɇP�q�۵���� �l�eQ����y�9�pT�ag�� �)跁���;��g8����V�����1	���p�30�9�j�$�D�Z�s����@�]��Z��ڒ&cxqφ� k~���A|T�&,/�sٙ�|o:6�l�=�X�( ��gy0��q~�n)H��<\G/C�Xs �.ˣ�94� mBu�j��������&X$�,[�1'P��b����Z@�J��lj�1X��9/}l7R�\�K=���/��BNY	FS� �����Ĭ��,$OGˋ>��%A�G��ן(O�%�5�$���8-���T�e� ��ϥHz-�M@<+a1B��;�d�q�����ƚ���f��'�4s�A&�%fm�afP`����r��\(�`=a;_��o>]!@�"�����J���	��-E��n��Q����������hV�+\*p���f�e����"�\j8����r�-H���"����u�`��xĐ$*��s	B�^�e���Ǖ�ܑN$8s$��
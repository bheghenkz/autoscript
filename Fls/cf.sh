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
BZh91AY&SYǘMj  ��0 @}������~����PoP��	H���S50#@��OS4bi��1@ѡ�&������F�FL�a �s	�#CC!�hd4Ѡ� @0�h����a4h �d�T��b�i��56#S#L�4f��F�Q�546� $�V<z�|�q���)C^��_�����E��zk'����T�,=f���wDu�o����pG��3T7J��%�,�aw6�d�����x�d�j���F��ˆP�Ć���&���j���"H�w��4%*��򓚓fEIQ�Ȍo��Lԝ/����7L�ġ}�&���T����q�Zm6����^ŉ�|�`��Xh�a�k�@�#�U�X�o���|���4���m��%=x���Vj<�:3� �𣐒�z\��^�6=���>����׀�T�aЊ<z_�Z�[����%�[�޺�f�>,��Y1(G����.F{aq='��`ܾKܔ�P��*ũ.0�����]82�O��G˴Xf�a 7���W�s @����-E�_b��֫V.VDYGt��{�oN$�	p>�̲���¥L\�	R�(Ѽ҈�#�����_9MX�*�z�:e~��FZG)��L�K�5�����Zٜ�hX���ƥ��,'��5�Z#/���>�o>�v�7�ؾo�&�ЕV�b#�9u�6�rC�37!w�#�ò�9���RN��؉�$I�4���$���E��m��w3�R�Ȝ�͂��m�NE�Y.dF}{�锑!�0�%��K��q���*م��=&�����������ZE7{��,9=��.�+3�'-�2���"�����WŊ4T�d�0�ޕ
/m]�3��a��dYg��ؽ�q��c����6n4yW���3�����П�tD(��L����h����]��BCa5�
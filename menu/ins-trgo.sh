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
BZh91AY&SY^j;� @߀P}���?�_�����P=���7kos;c{z^ޘh�=@ښ i�h       C�(�4F�� ���F�=D�&I����h4��"%4jz�O�Q�=@�ѡ�z�� 44�5�I�zFM�膌� 4 4d��lY�� �L�n�>�)�)���Nh�~�j{X�TH&'�H#�#���+%Q�1�u�!)HK��6vBa9/�LY�'��ŷ��'S�q&��W��&�[3<N��.�I�x�[�RE)z3'#�W�jO�U�Q��q�]f0�*d�6���]�`��K��ܟ�*i�5��f��*�r��T~�Z0�΄��:N�$Ia$lcl�D���gR�^ʻ�N8=
����Z߲`i�GG,r��n�+�7]z�A	/bC�t�Fr�dYbP0���"�C�4�9���O5�T��-U%�

O�E�^g�rr�"2�+�m�����SX��(t*D��#�F�$�i�9gy�w؀V��5n����ezh�t?��8�/P����R�s�"E�ho�*�2��}O�����23��2��s�2qm�`�`�äflf�x}o����ն�J-�t�z��p(�����I�q�2{@n0�������`Ԋ�\%ھ��6�;�޳9�e3^D9��r�6��U��dB�Tdq]�����V�L��Ǉ�s��xX�x�d�|��@9J���p�cb�^�&^V�w���}R��l Ui�M�����i�ӿ�a[6g>`�	�2Gqch媰�*]s����q���M�\J�8ŒTS�C�E�pmx�`��	�̵��@�3G15_X�8Q,.40�ߘ�<X�p�;j	uF�?]N���p9�I�W9Z��S��lԥ+9��x�'� 4���K��M2�i��J�:5Lh��)�����0h�L��!9v	y�����K��Ml#���:x\9j�����3L�!9CM�Z1�I�Vo�EAZ��钚�j�PI�v�'���$ B��J��U�MȘI *��Av�,9�ӻǨet7�2<�K��hC\���m�������`*�W(XЄA8ɕ���R2qDml
��af�\㿑�L��W������"k��R��@,��+�2�Z��'[g(ITP����څTg%�̌&��,/�1o&��y�Q�+i�c����Q�te����!c��2�i�3ZFH��6b/Ka�i��cR:�"m��LD����؅ae�69y��4���{>Z��e׈Ps�SV���L���2����c��C�T�B_��'!����-cf�;z$�*���"�(H/5��
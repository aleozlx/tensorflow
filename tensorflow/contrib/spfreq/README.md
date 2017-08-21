# Superpixel pooling

...

### Usage

...


bazel build --config opt --config cuda //tensorflow/contrib/spfreq:ops/_spfreq_ops.so
bazel test --config opt --config cuda -k //tensorflow/contrib/spfreq:spfreq_ops_test

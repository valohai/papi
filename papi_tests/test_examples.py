def test_example1():
    from papi_examples.example1 import example1

    p = example1()
    # Make sure there are no _1 suffixes when not needed
    assert set(p.nodes) == {"evaluate", "batch_feature_extraction", "train_model"}

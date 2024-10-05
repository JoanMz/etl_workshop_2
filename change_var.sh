echo ""

if [ "$AIRFLOW_HOME" != "$(pwd)" ]; then
        export AIRFLOW_HOME=$(pwd)/Dags
fi


echo "AIRFLOW HOME VARIABLE SET:"
echo ""
echo $AIRFLOW_HOME
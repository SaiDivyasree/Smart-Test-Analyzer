package tests;

import java.io.FileWriter;
import java.io.IOException;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.ITestResult;
import org.testng.annotations.AfterMethod;
import org.testng.annotations.BeforeMethod;
import org.testng.annotations.Test;

public class LoginTest {
    WebDriver driver;

    @BeforeMethod
    public void setup() {
        System.setProperty("webdriver.chrome.driver", "chromedriver.exe");
        driver = new ChromeDriver();
    }

    @Test
    public void testLoginFail() {
        driver.get("https://opensource-demo.orangehrmlive.com");
        driver.findElement(By.id("username")).sendKeys("admin"); // wrong ID to fail
    }

    @Test
    public void testMissingElement() {
        driver.get("https://opensource-demo.orangehrmlive.com");
        driver.findElement(By.id("nonexistent")).click();  // NoSuchElementException
    }


    @AfterMethod
    public void teardown(ITestResult result) {
        if (result.getStatus() == ITestResult.FAILURE) {
            try (FileWriter fw = new FileWriter("logs/failed_logs.txt",true)) {
                // ✅ Write test name
                fw.write("TEST: " + result.getName() + "\n");

                // ✅ Write the error message
                Throwable exception = result.getThrowable();
                fw.write("ERROR: " + exception.toString() + "\n");

                // ✅ Extract stack trace for line, method, and class
                StackTraceElement[] stackTrace = exception.getStackTrace();

                for (StackTraceElement element : stackTrace) {
                    // 🔍 Only log your actual test class (skip internals)
                    if (element.getClassName().contains("LoginTest")) {
                        fw.write("CLASS: " + element.getClassName() + "\n");
                        fw.write("METHOD: " + element.getMethodName() + "\n");
                        fw.write("LINE: " + element.getLineNumber() + "\n");
                        break;
                    }
                }

                fw.write("-----\n");

            } 
            catch (IOException ioEx) {
                ioEx.printStackTrace();
            }
        }

        // 🧹 Clean up browser or test state
        driver.quit(); // Only if you're using WebDriver instance
    }




}
